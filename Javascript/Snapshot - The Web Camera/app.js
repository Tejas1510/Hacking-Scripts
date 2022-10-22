const video = document.querySelector(".videoStream");

//Video Stream init
let faceUser = true;
let constraints = {
  audio: false,
  video: true,
  facingMode: faceUser ? "user" : "environment",
};

function handleSuccess(stream) {
  window.stream = stream; // make stream available to browser console
  video.srcObject = stream;
}

function handleError(error) {
  if (error.name.includes("NotAllowedError")) {
    console.log("Please allow to record video dumbass");
  }
}

navigator.mediaDevices
  .getUserMedia(constraints)
  .then(handleSuccess)
  .catch(handleError);

document.querySelector(".change-camera").addEventListener("click", () => {
  if (faceUser) faceUser = false;
  else faceUser = true;
  constraints = {
    audio: false,
    video: true,
    facingMode: faceUser ? "user" : "environment",
  };
  navigator.mediaDevices
    .getUserMedia(constraints)
    .then(handleSuccess)
    .catch(handleError);
});

//Image Capture Init
const canvas = document.querySelector(".shot");
document.querySelector(".capture-shot").addEventListener("click", () => {
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);
  document.querySelector(".instruct-container").style.display = "none";
  document.querySelector(".quick-image-editor").style.transform =
    "translateY(0)";
  var imgURL = canvas.toDataURL("image/png");
  img.src = imgURL;
  console.log(imgURL);
});

document.querySelector(".capture-video").addEventListener("click", () => {
  swal("Video Recording coming soon...");
});
