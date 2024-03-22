const Explanation = () => (
  <div style={{ marginTop: "3rem", marginBottom: "3rem", maxWidth: "850px" }}>
    <h3>How this works</h3>
    <p>
      These estimates are produced by an AI model trained on the{" "}
      <a href="https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.00522/full">
        The BEST Dataset of Language Proficiency
      </a>
      . This dataset contains information about 650 multilinguals from the
      Basque area of Spain, and provides an objective measures of English
      proficiency through a variety of rigorous tests.
    </p>
    <p>
      Though there is a huge variety in the proficiencies of learners, there is
      a clear correlation between the amount of time that people are exposed to
      English in their life and their proficiency level.
    </p>
    <img className="img-fluid mb-4" src="/fig-1.png" />
    <p>
      We can also view this relationship in terms of the violin or box plots we
      often see in statistics. The more people are exposed to English, the
      higher the probability there is of a higher English proficiency.
    </p>
    <img className="img-fluid mb-4" src="/fig-4.png" />
    <p>
      There are also more moderate correlations to language proficiency with
      people's age and education levels.
    </p>
    <div className="row mb-2">
      <div className="col">
        <img className="img-fluid" src="/fig-3.png" />
      </div>
      <div className="col">
        <img className="img-fluid" src="/fig-2.png" />
      </div>
    </div>
    <p>
      We can see that these factors of age and education aren't as important,
      because they don't appear to affect proficiency as much. The blue line is
      not as steep.
    </p>
    <p>
      The blue line in these diagrams is what we might call a{" "}
      <em>linear regression</em>. You can follow it to make general predictions
      about what the y value will most probably be for any given x value. For
      instance, in the first chart above, we can see that if someone spends 40%
      of their time exposed to English, they will <em>most likely</em> have an
      80% proficiency in English.
    </p>
    <p>
      We can also draw these <em>regressions</em> in a 3d space if we want to
      predict what z would be given <em>two other variables</em> x and y. For
      instance, here is an example of a regression for language proficiency
      based on age and percentage of time exposed to English.
    </p>
    <img className="img-fluid" src="/fig-5.png" />
    <img className="img-fluid mb-4" src="/fig-5.gif" />
    <p>
      With this kind of model, we can follow the blue regression pane to see
      what the proficiency would most likely be given an certain age and English
      exposure percentage.
    </p>
    <p>
      The model used in the estimation does the same thing,{" "}
      <em>but in a 4D space</em>, which of course is harder to visualize or
      imagine. The 4D model also provides us with a slightly better{" "}
      <strong>R² score of 0.20</strong>.
    </p>
  </div>
);

export default Explanation;
