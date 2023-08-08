let imageUPloaerImage = document.querySelectorAll('.imageUPloaerImage')
let imageUploader = document.querySelectorAll('.imageUploader')

window.addEventListener('load', function() {
    imageUploader.forEach((imageUploader,index)=>{

        imageUploader.addEventListener('change', function() {
            if (this.files && this.files[0]) {
                imageUPloaerImage[index].onload = () => {
                    URL.revokeObjectURL(imageUPloaerImage[index].src);  // no longer needed, free memory
                }
      
                imageUPloaerImage[index].src = URL.createObjectURL(this.files[0]); // set src to blob url
            }
        });
    })
  });
console.log('imageUploader')