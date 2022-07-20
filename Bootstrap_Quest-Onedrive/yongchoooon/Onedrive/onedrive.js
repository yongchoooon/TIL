function drag(e) {
  e.dataTransfer.setData("Text", e.target.id);
}