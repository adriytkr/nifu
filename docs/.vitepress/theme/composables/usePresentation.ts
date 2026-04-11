import {ref} from 'vue';

export function usePresentation(totalSlides:number){
  const iframeRef=ref<HTMLIFrameElement|null>(null);

  const currentSlide=ref(0);

  const isPlaying=ref(false);
  const isStarted=ref(false);

  function start(){
    isPlaying.value=true;
    isStarted.value=true;
  }

  function firstSlide(){
    currentSlide.value=0;

    if(iframeRef.value?.contentWindow){
      const method=JSON.stringify({ method: 'slide',args:[0] });
      iframeRef.value.contentWindow.postMessage(method,'*');
    }
  }

  function previousSlide(){
    if(currentSlide.value-1<0)return;

    currentSlide.value--;

    if(iframeRef.value?.contentWindow){
      const method=JSON.stringify({ method: 'prev' });
      iframeRef.value.contentWindow.postMessage(method,'*');
    }
  }

  function nextSlide(){
    if(currentSlide.value+1>=totalSlides)return;

    currentSlide.value++;

    if(iframeRef.value?.contentWindow){
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

  return{
    iframeRef,
    isStarted,
    start,

    currentSlide,

    isPlaying,
    togglePlay,

    previousSlide,
    nextSlide,
    firstSlide,
    lastSlide,
  };
}
