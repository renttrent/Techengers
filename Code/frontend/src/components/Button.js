export default function Button({ name }) {
  // u can get props like Button(props) and access props.name or
  // {name} <- destructering props to get only 'name' variable
  // https://reactjs.org/docs/components-and-props.html
  return (
    <div>
      <button>{name}</button>
    </div>
  );
}
