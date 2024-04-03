// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.querySelector("#word-form");
//   const resultDiv = document.querySelector("#result");

//   form.addEventListener("submit", async function (e) {
//     e.preventDefault();
//     const word = form.elements.word.value;
//     const res = await axios.get(`/check-word?word=${word}`);
//     resultDiv.innerText = res.data.result;
//   });
// });

// let score = 0;

// // Inside the form submit event listener, after getting the result:
// if (res.data.result === "ok") {
//   score += word.length;
//   document.querySelector("#score").innerText = `Score: ${score}`;
// }
// setTimeout(function () {
//   form.elements.word.disabled = true;
//   form.elements.submit.disabled = true;
// }, 60000);

// setTimeout(function () {
//   axios.post("/post-score", { score: score }).then(function (response) {
//     if (response.data.newRecord) {
//       alert("New record!");
//     }
//   });
// }, 60000);
document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("#word-form");
  const resultDiv = document.querySelector("#result");
  let score = 0;

  form.addEventListener("submit", async function (e) {
    e.preventDefault();
    const word = form.elements.word.value;
    const res = await axios.get(`/check-word?word=${word}`);

    if (res.data.result === "ok") {
      score += word.length;
      document.querySelector("#score").innerText = `Score: ${score}`;
    }
    resultDiv.innerText = res.data.result;
  });

  setTimeout(function () {
    form.elements.word.disabled = true;
    form.elements.submit.disabled = true;
    axios.post("/post-score", { score: score }).then(function (response) {
      if (response.data.newRecord) {
        alert("New record!");
      }
    });
  }, 60000);
});
