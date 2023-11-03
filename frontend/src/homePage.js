import React from 'react';
import { useState } from 'react';
import { useNavigate } from "react-router";
import ProjectTable from './Projects';
import Button from '@mui/material/Button';


function HomePage(props) {
  const navigate = useNavigate();

  const projects = [
    {
      id: 1,
      name: 'Project 1',
      user: 'abc',
    },
    {
      id: 2,
      name: 'Project 2',
      user: 'def'
    },
    {
      id: 3,
      name: 'Project 3',
      user: 'ghi'
    },
    {
      id: 3,
      name: 'Project 3',
      user: 'ghi'
    },
    {
      id: 3,
      name: 'Project 3',
      user: 'ghi'
    },
    {
      id: 3,
      name: 'Project 3',
      user: 'ghi'
    },
    {
      id: 3,
      name: 'Project 3',
      user: 'ghi'
    },
    {
      id: 3,
      name: 'Project 3',
      user: 'ghi'
    }
  ];

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
                  <Button variant="contained" color="primary" href="/addProject">Add Project</Button>
                </div>
            </div>
        </div>
    </div>

    );
}

export default HomePage;
