import Explanation from "./components/Explanation";
import Estimator from "./components/Estimator";

function App() {
  return (
    <div className="container">
      <div className="my-5">
        <h2>Language Proficiency Estimator</h2>
        <p className="lead">
          Estimates expected proficiency level based on life profile
        </p>
        <p>
          (for educated adults with exposure to English as a foreign language
          before the age of 12)
        </p>
      </div>
      <Estimator />
      <Explanation />
      <p className="mb-4 small">
        This application was developed by Adam Dueck.{" "}
        <a href="https://github.com/adueck/language-proficiency-estimator">
          Source code available on GitHub
        </a>
        .
      </p>
    </div>
  );
}

export default App;
