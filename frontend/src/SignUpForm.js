import { useState } from 'react';
import { useNavigate } from "react-router";
function SignUpForm() {
  const navigate = useNavigate();

  const [username, setUsername] = useState('');
  const [userID, setUserID] = useState('');
  const [password, setPassword] = useState('');
  const [secondPassword, setSecondPassword] = useState('');


  const handleUsername = (e) => {
    setUsername(e.target.value); 
  }

  const handlePassword = (e) => {
    setPassword(e.target.value); 
  }

  const handleSecondPassword = (e) => {
    setSecondPassword(e.target.value); 
  }

  const handleUserID = (e) => {
    setUserID(e.target.value); 
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    if(password !== secondPassword) {
      alert("Entered passwords do not match");
      return;
    }

    if(username === '' || password === '' || userID === '' || secondPassword === '') {
      alert("All fields were not filled out");
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
          body: JSON.stringify({ userName:username, password:password, userID:userID })
      });

      const data = await response.json();
      console.log(data.message);

      if (data.message === "User registered successfully") {
          alert("User registered successfully")
          navigate('/');
      } else if (data.message === "Username has already been taken") {
          alert("User already exists");
      } else {
          alert("An error occured: " + data.message);
      }
    } catch (err) {
      console.error(err);
    }
  };

    return (
    <div className="flex justify-center items-center h-screen w-screen">
    <div className="border-t-8 rounded-md border-amber-600 bg-white p-14 shadow-2xl w-96">
      <div className="SignUpForm">
        <header className="SignUpForm-header">
          <h1 className="font-bold text-center block text-3xl">Sign Up</h1>
            <div>
              <label className="text-gray-500 block mt-3">User ID</label>
              <input className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100" type="text"
                placeholder='Enter your User ID'
                style={{marginRight:'10px'}}
                value={userID}
                onChange={handleUserID}
              />
            </div>
            <div>
              <label className="text-gray-500 block mt-3">Username</label>
              <input className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100" type="text"
                placeholder='Enter your desired username'
                value={username}
                onChange={handleUsername}
              />
            </div>
            <div>
              <label className="text-gray-500 block mt-3">Password</label>
              <input type="password"
                placeholder='Enter your desired password'
                value={password}
                onChange={handlePassword}
                className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100" 
              />
            </div>
            <div>
            <label className="text-gray-500 block mt-3">Re-enter Password</label>
              <input type="password"
                placeholder='Enter password again'
                value={secondPassword}
                onChange={handleSecondPassword}
                className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100"
              />
            </div>
            <button className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-amber-600 to-red-400 hover:from-amber-700 hover:to-red-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg" type="submit" onClick={() => {navigate('/')}} style={{marginRight:'20px'}}>Back</button>
            <button className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-amber-600 to-red-400 hover:from-amber-700 hover:to-red-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg" type="submit" onClick={handleSubmit} style={{marginRight:'20px'}}>Submit</button>
        </header>
      </div>
    </div>
    </div>
    );
};

export default SignUpForm;