import Navbar from "./components/Navbar";
import Button from "./components/Button";

// Run with npm run start at */Code/frontend path
// localhost:3000 will open automatically in browser

function App() {
  return (
    <div>
      {/* This is a component */}
      <Navbar />
      <p>Hello Soft Eng</p>
      {/* Component with props */}
      <Button name="Yes" />

      <Button name="No" />
    </div>
  );
}

export default App;
