import { useState } from 'react';
import { useNavigate } from "react-router";

function SignUpForm() {
  const navigate = useNavigate();

    return (
    <div className="SignUpForm">
      <header className="SignUpForm-header">
        <h1>Sign Up</h1>
          <div>
            <label>First Name</label>
            <input type="text"
              placeholder='Enter your first name'
              style={{marginRight:'10px'}}
            />
          </div>
          <div>
            <label>Username</label>
            <input type="text"
              placeholder='Enter your desired username'
            />
          </div>
          <div>
            <label>Password</label>
            <input type="password"
              placeholder='Enter your desired password'
            />
          </div>
          <div>
          <label>Re-enter Password</label>
            <input type="password"
              placeholder='Enter password again'
            />
          </div>
          <div>
            <label>E-mail</label>
            <input type="email"
              placeholder='Enter your e-mail addresss'
            />
          </div>
          <button type="submit" onClick={() => {navigate('/')}} style={{marginRight:'20px'}}>Back</button>
          <button type="submit" style={{marginRight:'20px'}}>Submit</button>
      </header>
    </div>
    );
};

export default SignUpForm;