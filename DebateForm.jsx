import React, { useState } from "react";
import { getDebate } from "../services/api";
import ResultCard from "./ResultCard";

function DebateForm() {
  const [topic, setTopic] = useState("");
  const [result, setResult] = useState("");

  const handleSubmit = async () => {
    const res = await getDebate(topic);
    setResult(res.result);
  };

  return (
    <div>
      <input
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Enter topic..."
      />
      <button onClick={handleSubmit}>Generate</button>

      {result && <ResultCard result={result} />}
    </div>
  );
}

export default DebateForm;