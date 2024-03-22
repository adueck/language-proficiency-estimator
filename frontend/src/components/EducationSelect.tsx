function EducationSelect({
  value,
  onChange,
}: {
  value: EducationLevel | undefined;
  onChange: (value: EducationLevel) => void;
}) {
  const options = [
    "High School",
    "Professional Training",
    "University",
    "Postgraduate",
  ];
  const onOptionChangeHandler = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const educationLevel = parseInt(e.target.value) as EducationLevel;
    return onChange(educationLevel);
  };
  return (
    <select
      value={value}
      onChange={onOptionChangeHandler}
      className="form-select"
    >
      {value === undefined && <option>Please choose education</option>}
      {options.map((option, index) => {
        return (
          <option key={index} value={index}>
            {option}
          </option>
        );
      })}
    </select>
  );
}

export default EducationSelect;
