import { useState } from "react";
import EducationSelect from "./EducationSelect";

const MIN_AGE = 18;
const MAX_AGE = 50;
const MIN_PERCENT = 1;
const MAX_PERCENT = 70;

function validate(
  n: number | undefined,
  min: number,
  max: number
): n is number {
  return !!(n !== undefined && min <= n && max >= n);
}

function Estimator() {
  const [age, setAge] = useState<number | undefined>(undefined);
  const [education, setEducation] = useState<number | undefined>(undefined);
  const [percent, setPercent] = useState<number | undefined>(undefined);
  const [proficiency, setProficiency] = useState<
    number | undefined | "calculating..."
  >(undefined);
  const [message, setMessage] = useState<string>("");
  function changeField(f: "age" | "education" | "percent", val: number) {
    setMessage("");
    if (f === "age") {
      setAge(val);
    } else if (f === "education") {
      setEducation(val);
    } else {
      setPercent(val);
    }
  }
  async function fetchPrediction(request: PredictionRequest) {
    const t = setTimeout(() => {
      setProficiency("calculating...");
    }, 200);
    try {
      const res = await fetch(
        import.meta.env.VITE_PROFICIENCY_API || "http://localhost:5000",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(request),
        }
      );
      const { proficiency } = (await res.json()) as PredictionResponse;
      clearTimeout(t);
      setProficiency(proficiency);
    } catch (e) {
      alert("connection error - check internet connection");
    }
  }
  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    if (!validate(age, MIN_AGE, MAX_AGE)) {
      setMessage("Please enter a valid age");
      return;
    }
    if (!validate(percent, MIN_PERCENT, MAX_PERCENT)) {
      setMessage("Please enter a valid number for English exposure percentage");
      return;
    }
    if (education === undefined) {
      setMessage("Please select an education level");
      return;
    }
    // Form valid - proceed with submission to API for estimation
    const request: PredictionRequest = { age, education, percent };
    fetchPrediction(request);
  }

  return (
    <>
      {" "}
      <div>
        <form onSubmit={handleSubmit} style={{ maxWidth: "400px" }}>
          <div className="mb-3">
            <label htmlFor="age" className="form-label">
              Age: ({MIN_AGE}-{MAX_AGE})
            </label>
            <input
              value={age}
              onChange={(e) => changeField("age", parseInt(e.target.value))}
              type="number"
              className="form-control"
              id="age"
              min={MIN_AGE}
              max={MAX_AGE}
            />
          </div>
          <div className="mb-3">
            <label htmlFor="age" className="form-label">
              Education level:
            </label>
            <EducationSelect
              value={education}
              onChange={(v) => changeField("education", v)}
            />
          </div>
          <div className="mb-3">
            <label htmlFor="age" className="form-label">
              Percentage of English exposure in everday life: ({MIN_PERCENT}-
              {MAX_PERCENT})
            </label>
            <input
              type="number"
              className="form-control"
              onChange={(e) => changeField("percent", parseInt(e.target.value))}
              value={percent}
              id="percent"
              min={MIN_PERCENT}
              max={MAX_PERCENT}
            />
          </div>
          {message && (
            <div className="alert alert-warning" role="alert">
              {message}
            </div>
          )}
          <button type="submit" className="btn btn-primary">
            Estimate
          </button>
        </form>
      </div>
      <p className="mb-4 mt-3">
        {proficiency && (
          <span>
            Expected proficiency level: {proficiency}
            {typeof proficiency === "number"}%
          </span>
        )}
      </p>
    </>
  );
}

export default Estimator;
