import { useState } from 'react'
import Navbar from './Navbar.jsx'
import './App.css'

function App() {
  return (
    <div className='flex flex-col max-w-screen max-h-screen'>
      <Navbar/>
      <div className="card max-w-screen shadow-xl h-screen bg-base-300">
        <div className="card-body">
          <h2 className="card-title">Card title!</h2>
          <p>If a dog chews shoes whose shoes does he choose?</p>
          <div className="card-actions justify-end">
            <button className="btn btn-primary">Buy Now</button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
