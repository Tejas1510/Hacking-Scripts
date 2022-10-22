let adjust = {
    brightness: 0.5,
    contrast: 0.5,
    saturation: 0.5,
    sepia: 0,
  },
  img = new Image();

document.querySelector(".retake-btn").addEventListener("click", () => {
  canvas.getContext("2d").clearRect(0, 0, canvas.width, canvas.height);
  document.querySelector(".instruct-container").style.display = "flex";
  document.querySelector(".quick-image-editor").style.transform =
    "translateY(150%)";
});

document.querySelector(".save-btn").addEventListener("click", () => {
  var imgURL = canvas.toDataURL("image/png");
  download(imgURL);
});

document
  .querySelector(".brightness-slider input")
  .addEventListener("input", (s) => {
    document.querySelector(".brightness-slider .progress").style.width =
      document.querySelector(".brightness-slider input").value * 100 + "%";
    adjust["brightness"] = document.querySelector(
      ".brightness-slider input"
    ).value;
    editImage();
  });
document
  .querySelector(".contrast-slider input")
  .addEventListener("input", (s) => {
    document.querySelector(".contrast-slider .progress").style.width =
      document.querySelector(".contrast-slider input").value * 100 + "%";
    adjust["contrast"] = document.querySelector(".contrast-slider input").value;
    editImage();
  });
document
  .querySelector(".saturation-slider input")
  .addEventListener("input", (s) => {
    document.querySelector(".saturation-slider .progress").style.width =
      document.querySelector(".saturation-slider input").value * 100 + "%";
    adjust["saturation"] = document.querySelector(
      ".saturation-slider input"
    ).value;
    editImage();
  });
document.querySelector(".sepia-slider input").addEventListener("input", (s) => {
  document.querySelector(".sepia-slider .progress").style.width =
    document.querySelector(".sepia-slider input").value * 100 + "%";
  adjust["sepia"] = document.querySelector(".sepia-slider input").value;
  editImage();
});

function editImage() {
  canvas.getContext("2d").filter =
    "brightness(" +
    adjust["brightness"] * 2 +
    ") contrast(" +
    adjust["contrast"] * 2 +
    ") saturate(" +
    adjust["saturation"] * 2 +
    ") sepia(" +
    adjust["sepia"] +
    ")";
  canvas.getContext("2d").drawImage(img, 0, 0, canvas.width, canvas.height);
}
