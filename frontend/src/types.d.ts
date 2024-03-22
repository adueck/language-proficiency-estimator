type PredictionRequest = {
  age: number;
  education: EducationLevel;
  percent: number;
};

enum EducationLevel {
  HighSchool,
  ProfessionalTraining,
  University,
  Postgraduate,
}

type PredictionResponse = {
  proficiency: number;
};
