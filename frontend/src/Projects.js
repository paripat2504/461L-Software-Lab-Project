
import { useState } from 'react'; 
import Button from '@mui/material/Button';

function Project({project}) {
    

    return (
        <div className="bg-amber-500 flex justify-center rounded-xl h-1/3 p-4 shadow-md my-4">
              <div className="columns-3">
                <div className="flex flex-col max-w-xs">
                    <p className="text-lg font-bold">{project.projectName}</p>
                    <p className="text-base overflow-auto">{project.projectDescription}</p>
                </div>
                <div className="flex flex-col">
                    <p className="text-lg font-bold">{project.Computers_CheckedOut}</p>
                    <p className="text-base">Computers Used</p>
                </div>
                <div className="flex flex-col">
                    <p className="text-lg font-bold">{project.Servers_CheckedOut}</p>
                    <p className="text-base">Servers Used</p>
                </div>
                <div className="justify-center">
                  <Button variant="contained" color="primary">Manage Resources</Button>
                  <div className='pt-4'/>
                  <Button variant="contained" color="primary">Leave Project</Button>
                </div>
              </div>
        </div>
    );
}

function ProjectTable({ projects }) {
  return (
    <div>
      {projects.length === 0 ? (
        <p className="text-base justify-center flex font-bold">No projects to display. Join or create one!</p>
      ) : (
        projects.map((project) => (
          <Project key={project.projectID} project={project} />
        ))
      )}
    </div>
  );
}


export default ProjectTable;