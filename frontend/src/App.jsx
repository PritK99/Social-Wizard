import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from './Navbar.jsx'
import HomePage from "./HomePage.jsx";
import './App.css'
import Audience from "./Audience.jsx";
import Content from "./Content.jsx";

function App() {
  return (
    <div className='flex flex-col max-w-screen max-h-screen'>
      <Router>
        <Navbar/>
        <Routes>
          <Route path="/" element={<HomePage/>}></Route>
          <Route path="/audience" element={<Audience/>}></Route>
          <Route path="/content-gen" element={<Content/>}></Route>
        </Routes>
      </Router>
      
    </div>
  )
}

export default App
