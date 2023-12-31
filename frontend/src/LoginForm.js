import { useState } from 'react'; 
import { useNavigate } from "react-router";
import { useAuth } from './UserContext';

function LoginForm() {
    const { login } = useAuth();
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    //Make sure localstorage is clear
    localStorage.removeItem('userId');
    localStorage.removeItem('userName');
    localStorage.removeItem('projectsData');
    localStorage.removeItem('hardwareData');
  
    const handleUsername = (e) => {
      setUsername(e.target.value); 
    }
  
    const handlePassword = (e) => {
      setPassword(e.target.value); 
    }
  
    const handleLogin = async (e) => {
        e.preventDefault();
        if(username === '' || password === '') {
          setMessage("Please fill out all fields");
          return;
        }
        try {
          const response = await fetch('https://mysterious-everglades-11029-c622e00a9e3b.herokuapp.com/login', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ userID:username, password })
          });
        
          const data = await response.json();
          //Handle message
          if (data.message === "Login successful") {
            login(username, data.userName);
            navigate('/home');
          } else {
            setMessage(data.message);
          }
        } catch (err) {
          console.error(err);
          setMessage("An error occured: " + err)
        };
    };

    const handleSignupClick = () => {
      navigate('/signup');
    };
  
    return (
      <div className="flex justify-center items-center h-screen w-screen">
      <div className=" border-t-8 rounded-md border-amber-600 bg-white p-14 shadow-2xl w-96">
      <form onSubmit={handleLogin}>
        <h1 className="font-bold text-center block text-3xl">Log In</h1>
          <div>
            <label className="text-gray-500 block mt-3">User ID</label>
            <input className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100" type="text"
              placeholder='Enter your User ID'
              style={{marginRight:'10px'}}
              value={username}
              onChange={handleUsername}
            />
          </div>
          <div>
            <label className="text-gray-500 block mt-3">Password</label>
            <input className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100" type="password"
              placeholder='Enter your password'
              value={password}
              onChange={handlePassword}  
            />
          </div>
          <div className="text-red-600 flex justify-center">{message}</div>
          <button type="submit" className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-amber-600 to-red-400 hover:from-amber-700 hover:to-red-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg" onClick={handleLogin} style={{marginRight:'20px'}}>Submit</button>
          <button type="button" className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-amber-600 to-red-400 hover:from-amber-700 hover:to-red-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg"onClick={handleSignupClick}>Sign up</button>
          
    </form>
    </div>
    </div>
    );
  }
  
  export default LoginForm;