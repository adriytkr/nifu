import { nextTick, onMounted, onUnmounted, ref } from 'vue';

export function useSlides(totalSlides:number){
  const videoRef=ref<HTMLDListElement|null>(null);
  const videoContainerRef=ref<HTMLDListElement|null>(null);
  const isFullScreen=ref(false);

  function handleFullScreen(){
    isFullScreen.value=!!document.fullscreenElement;
  }

  function enterFullScreen(){
    // videoRef.value?.requestFullscreen();
    videoContainerRef.value?.requestFullscreen();
    videoRef.value?.focus();
    isFullScreen.value=true;
  }

  function leaveFullScreen(){
    document.exitFullscreen();
    isFullScreen.value=false;
  }

  function toggleFullScreen(){
    isFullScreen.value=!isFullScreen.value;

    if(isFullScreen.value){
      enterFullScreen();
      return;
    }

    leaveFullScreen();
  }

  const iframeRef=ref<HTMLIFrameElement|null>(null);

  const currentSlide=ref(0);

  const isPlaying=ref(false);
  const isStarted=ref(false);

  function start(){
    videoRef.value?.focus();

    isPlaying.value=true;
    isStarted.value=true;
  }

  function firstSlide(){
    currentSlide.value=0;

    if(iframeRef.value?.contentWindow){
      // iframeRef.value.contentWindow.focus();

      const method=JSON.stringify({ method: 'slide',args:[0] });
      iframeRef.value.contentWindow.postMessage(method,'*');
    }
  }

  function previousSlide(){
    if(currentSlide.value-1<0)return;

    currentSlide.value--;

    if(iframeRef.value?.contentWindow){
      // iframeRef.value.contentWindow.focus();

      const method=JSON.stringify({ method: 'prev' });
      iframeRef.value.contentWindow.postMessage(method,'*');
    }
  }

  function nextSlide(){
    if(currentSlide.value+1>=totalSlides)return;

    currentSlide.value++;

    if(iframeRef.value?.contentWindow){
      // iframeRef.value.contentWindow.focus();

      const method=JSON.stringify({ method: 'next' });
      iframeRef.value.contentWindow.postMessage(method,'*');
    }
  }

  function play(){
    if(!isStarted.value)start();

    if(iframeRef.value?.contentWindow){
      const method=JSON.stringify({ method: 'triggerKey',args:[32] });
      iframeRef.value.contentWindow.postMessage(method,'*');
    }
  }

  function pause(){
    if(iframeRef.value?.contentWindow){
      const method=JSON.stringify({ method: 'triggerKey',args:[32] });
      iframeRef.value.contentWindow.postMessage(method,'*');
    }
  }

  function togglePlay(){
    isPlaying.value=!isPlaying.value;

    if(isPlaying.value){
      play();
      return;
    }

    pause();
  }

  function lastSlide(){
    currentSlide.value=totalSlides-1;

    if(iframeRef.value?.contentWindow){
      // iframeRef.value.contentWindow.focus();

      const method=JSON.stringify({ method: 'slide',args:[totalSlides-1] });
      iframeRef.value.contentWindow.postMessage(method,'*');
    }
  }

  function handleMessage(event:MessageEvent){
    const data=JSON.parse(event.data);

    const checkSlideChanged=
      data.namespace==='reveal'&&
      data.eventName==='slidechanged';

    if(checkSlideChanged)
      currentSlide.value=data.state.indexh;
  }

  function handleShortcut(event:KeyboardEvent){
    event.preventDefault();

    switch(event.code){
      case 'ArrowRight':
        nextSlide();
        break;
      case 'ArrowLeft':
        previousSlide();
        break;
      case 'ArrowUp':
        firstSlide();
        break;
      case 'ArrowDown':
        lastSlide();
        break;
      case 'KeyF':
        toggleFullScreen();
        break;
      case 'Space':
        togglePlay();
        break;
    }
  }

  onMounted(()=>{
    window.addEventListener('message',handleMessage);
    document.addEventListener('fullscreenchange',handleFullScreen)
  });

  onUnmounted(()=>{
    window.removeEventListener('message',handleMessage)
    document.removeEventListener('fullscreenchange',handleFullScreen)
  });

  return{
    iframeRef,
    isStarted,
    start,
    currentSlide,
    isPlaying,
    firstSlide,
    previousSlide,
    togglePlay,
    nextSlide,
    lastSlide,
    videoRef,
    isFullScreen,
    enterFullScreen,
    leaveFullScreen,
    toggleFullScreen,
    handleShortcut,
    videoContainerRef
  };
}
