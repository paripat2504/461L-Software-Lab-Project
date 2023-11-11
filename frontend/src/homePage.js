import React from 'react';
import { useNavigate } from "react-router";
import ProjectTable from './Projects';
import Button from '@mui/material/Button';
import { useAuth } from './UserContext';
import { Navigate } from 'react-router-dom';
import {useState, useEffect } from 'react';
import JoinProject from './JoinProject';
import AddProject from './AddProject';
import ResourceTable from './Resources';
import ManageResources from './ManageResources';

function useModal(initialState = false) {
  const [isOpen, setIsOpen] = useState(initialState);
  const openModal = () => setIsOpen(true);
  const closeModal = () => setIsOpen(false);
  return [isOpen, openModal, closeModal];
}

function HomePage() {
  const { userId, userName, logout } = useAuth();
  const navigate = useNavigate();
  const [isAddModalOpen, openAddModal, closeAddModal] = useModal(false);
  const [isJoinModalOpen, openJoinModal, closeJoinModal] = useModal(false);
  const [isHWModalOpen, openHWModal, closeHWModal] = useModal(false);
  const [proj, setProjects] = useState([]);
  const [resources, setResources] = useState([]);
  const [selectedProject, setSelectedProject] = useState(null);

  const handleManageResources = (project) => {
    setSelectedProject(project);
    openHWModal();
  };
  
  const fetchProjects = async () => {
    try {
      const response = await fetch('https://mejiasoftwareproject-ba462176bcee.herokuapp.com/displayProjects', {
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
  };

  const fetchResources = async () => {
    try {
      const response = await fetch('https://mejiasoftwareproject-ba462176bcee.herokuapp.com/displayHardware', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      });
      const data = await response.json();
      if (data.message === "Sucessfully Gathered Avaiabilities and Capacities") {
        localStorage.setItem('hardwareData', JSON.stringify(data.hw_dict));
        setResources(data)
      }
    } catch (err) {
      console.error(err);
      alert("An error occured: " + err)
    };
  };

  // USE EFFECT FOR PROJECTS
  useEffect(() => {
    const cachedProjects = localStorage.getItem('projectsData');
    if (cachedProjects) {
      // If cached data exists, use it and avoid making a new fetch request
      setProjects(JSON.parse(cachedProjects));
    } else if (userName) {
        fetchProjects();
    };
  }, [userName]);

  // USE EFFECT FOR HARDWARE RESOURCES
  useEffect(() => {
    const cachedResources = localStorage.getItem('hardwareData');
    if (cachedResources) {
      setResources(JSON.parse(cachedResources));
    } else {
      fetchResources();
    };
  }, []);


  if (userId === null) {
    //Navigate to login page
    return <Navigate to='/' />;
  }


  const handleLogout = () => {
    logout()
    localStorage.removeItem('projectsData');
    localStorage.removeItem('hardwareData');
    navigate('/');
  }
  
  const projects = proj;
    return (
    <div>    
       <div className="container mx-auto pt-14">
        <div className="flex">
          
          <div className="justify-center w-1/5 border-t-8 rounded-md bg-white h-128 p-5 mr-10 border-amber-600 items-center shadow-2xl">
            <p className="flex justify-center font-bold text-3xl">Resources</p>
            <div className="border-t-4 rounded-full border-slate-100 my-3 mb-5"/>
            <div className="overflow-y-auto h-4/5">
              <ResourceTable resources={resources}></ResourceTable>
            </div>
          </div>
  
          <div className="w-4/5 border-t-8  rounded-md border-amber-600 bg-white h-128 p-5 shadow-2xl">
            <p className="flex justify-center font-bold text-3xl">Projects</p>
            <div className="border-t-4 rounded-full border-slate-100 my-3"/>
            <div className="overflow-y-auto h-4/5">
              <ProjectTable projects={projects} onManageResources={handleManageResources}/>
              {selectedProject && (
                <ManageResources
                  isOpen={isHWModalOpen}
                  onRequestClose={() => {
                    closeHWModal();
                    setSelectedProject(null);
                  }}
                  project={selectedProject}
                />
              )}
            </div>
          </div>
        </div>
      </div>

        <div className="container mx-auto pt-10">
            <div className="flex justify-center">    
                <div className="w-95 border-t-8 rounded-md border-amber-600 bg-white h-24 p-5 shadow-2xl">
                  <div>
                    <Button variant="contained" color="primary" onClick={openAddModal}>Add Project</Button>
                    <AddProject fetchProjects={fetchProjects} isOpen={isAddModalOpen} onRequestClose={closeAddModal}/>
                  </div>
                  <div>
                    <Button variant="contained" color="primary" onClick={openJoinModal}>Join Project</Button>
                    <JoinProject fetchProjects={fetchProjects}  isOpen={isJoinModalOpen} onRequestClose={closeJoinModal}/>
                  </div>
                  <Button variant="contained" color="primary" onClick={handleLogout}>Sign Out</Button>
                </div>
            </div>
        </div>
    </div>

    );
}

export default HomePage;
