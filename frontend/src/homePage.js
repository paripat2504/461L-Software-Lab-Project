import React from 'react';
import { useNavigate } from "react-router";
import ProjectTable from './Projects';
import Button from '@mui/material/Button';
import { useAuth } from './UserContext';
import { Navigate } from 'react-router-dom';
import {useState, useEffect } from 'react';


import AddProject from './AddProject';

function HomePage(props) {
  const { userId, userName, logout } = useAuth();
  const navigate = useNavigate();
  const [isModalOpen, setIsModalOpen] = useState(false);
  const openModal = () => setIsModalOpen(true);
  const closeModal = () => setIsModalOpen(false);
  const [proj, setProjects] = useState([]);

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await fetch('http://localhost:5000/displayProjects', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ userName: userName })
        });
      
        const data = await response.json();

        if (data.message === "Project Retrieved successfully") {
          localStorage.setItem('projectsData', JSON.stringify(data.projects));
          setProjects(data.projects)
        }

      } catch (err) {
        console.error(err);
        alert("An error occured: " + err)
      };

    }
    
    const cachedProjects = localStorage.getItem('projectsData');

    if (cachedProjects) {
      // If cached data exists, use it and avoid making a new fetch request
      setProjects(JSON.parse(cachedProjects));
    } else if (userName) {
        fetchProjects();
    };
  }, [userName]);

  if (userId === null) {
    //Navigate to login page
    return <Navigate to='/' />;
  }

  const handleLogout = () => {
    logout()
    navigate('/');
  }

  const projects = [{Computers_CheckedOut:0, Servers_CheckedOut:0, 
                  Project_Name:'Project 1', Project_Description:'Project 1 Description', Project_ID:'1'}];


    return (
    <div>    
       <div className="container mx-auto pt-14">
        <div className="flex">
          
          <div className="justify-center w-1/5 border-t-8 rounded-md bg-white h-128 p-5 mr-10 border-amber-600 items-center shadow-2xl">
            <p className="flex justify-center font-bold text-3xl">Resources</p>
            <div className="border-t-4 rounded-full border-slate-100 my-3 mb-5"/>
            <div className="overflow-y-auto h-4/5">
                <p className="text-base">
                    Resources work in progress. 
                </p>
            </div>
          </div>
  
          <div className="w-4/5 border-t-8  rounded-md border-amber-600 bg-white h-128 p-5 shadow-2xl">
            <p className="flex justify-center font-bold text-3xl">Projects</p>
            <div className="border-t-4 rounded-full border-slate-100 my-3"/>
            <div className="overflow-y-auto h-4/5">
              <ProjectTable projects={projects}></ProjectTable>
            </div>
          </div>
        </div>
      </div>

        <div className="container mx-auto pt-10">
            <div className="flex justify-center">    
                <div className="w-95 border-t-8 rounded-md border-amber-600 bg-white h-24 p-5 shadow-2xl">
                  <div>
                    <Button variant="contained" color="primary" onClick={openModal}>Add Project</Button>
                    <AddProject isOpen={isModalOpen} onRequestClose={closeModal}/>
                  </div>
                  <Button variant="contained" color="primary" onClick={handleLogout}>Logout</Button>
                </div>
            </div>
        </div>
    </div>

    );
}

export default HomePage;
