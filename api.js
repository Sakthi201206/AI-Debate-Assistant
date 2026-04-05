export async function getDebate(topic) {
  const res = await fetch("http://127.0.0.1:8000/debate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ topic }),
  });

  return res.json();
}