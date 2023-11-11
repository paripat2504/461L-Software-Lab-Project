import Modal from 'react-modal';
import { useState } from 'react';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';



function ManageResourcesContent({ onRequestClose, project, fetchProjects, fetchResources }) {
    const [modalContent, setModalContent] = useState('default');
    const [qty, setQty] = useState('');
    const [message, setMessage] = useState('');
    const [selectedValue, setSelectedValue] = useState('Computers');

    // const express = require('express');
    // const cors = require('cors');
    // const app = express();

    // app.use(cors());

    const handleRadioChange = (event) => {
        setSelectedValue(event.target.value);
    };

    const handleConfirm = async (e) => {
        e.preventDefault();

        if(qty === '') {
            setMessage("Please enter a quantity");
        } else if (qty < 0) {
            setMessage("Please enter a positive quantity");
        //Make sure qty is a number
        } else if (qty % 1 !== 0) {
            setMessage("Please enter a whole number");
        }

        if(modalContent === 'checkIn') {
            //Check in hardware
            try {
              const jsonData = {
                projectID: project.projectID,
                hwSetID : selectedValue,
                amountRequested : qty
              }
                const response = await fetch(`http://127.0.0.1:5000/checkInHWSet`, {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json'

                  },
                  body: JSON.stringify(jsonData)
                });
              
                const data = await response.json();
                console.log(data)
                //Handle message
                alert(data.message);
                if(data.message === 'Hardware checked in successfully'){
                    onRequestClose();
                    setQty('');
                    setMessage('');
                    fetchProjects();
                    fetchResources();
                }
              } catch (err) {                                      
                console.error(err);
                alert("An error occured: " + err)
                onRequestClose();
              };
        } else if (modalContent === 'checkOut') {
            //Check out hardware
            try {
              const jsonData = {
                projectID: project.projectID,
                hwSetID : selectedValue,
                amountRequested : qty
              }
                const response = await fetch(`http://127.0.0.1:5000/checkOutHWSet`, {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify(jsonData)

                });
              
                const data = await response.json();
                console.log(data)
                //Handle message
                alert(data.message);
                if(data.message === 'Hardware checked out successfully'){
                    onRequestClose();
                    setQty('');
                    setMessage('');
                    fetchProjects();
                    fetchResources();
                }
              } catch (err) {                                      
                console.error(err);
                alert("An error occured: " + err)
                onRequestClose();
              };
        }

    }

    const handleQty = (e) => {
        setQty(e.target.value)
    }
  
    const handleCheckIn = () => {
      // Update the modal content for Check In
      setModalContent('checkIn');
    };
  
    const handleCheckOut = () => {
      // Update the modal content for Check Out
      setModalContent('checkOut');
    };
  
    return (
      <div className="border-t-8 rounded-md border-amber-600 bg-white p-14 shadow-2xl w-96 border-0 rounded-lg shadow-lg relative flex flex-col outline-none focus:outline-none">
        <button
          className="text-black h-6 w-6 text-4xl block outline-none focus:outline-none absolute top-1 right-5"
          onClick={onRequestClose}
        >
          ×
        </button>
        <form onSubmit={handleConfirm}>
          {/* DEFAULT CONTENT */}
          {modalContent === 'default' && (
              <div>
                    <h1 className="font-bold text-center block text-3xl">Manage Resources</h1>
                        <div>
                        <p className="text-base font-bold pt-4">Project Name</p>
                        <p className="text-base">{project.projectName}</p>
                    </div>
                    <div>
                        <p className="text-base font-bold pt-4">Project Description</p>
                        <p className="text-base">{project.projectDescription}</p>
                    </div>
                    <div>
                        <p className="text-base font-bold pt-4">Project ID</p>
                        <p className="text-base">{project.projectID}</p>
                    </div>
                    <div>
                        <p className="text-base font-bold pt-4">Computers Used</p>
                        <p className="text-base">{project.Computers_CheckedOut}</p>
                    </div>
                    <div>
                        <p className="text-base font-bold pt-4">Servers Used</p>
                        <p className="text-base">{project.Servers_CheckedOut}</p>
                    </div>
                    <div className="flex justify-center pt-4">
                        <button className="bg-amber-500 hover:bg-amber-700 text-white font-bold py-2 px-4 mx-2 rounded" onClick={handleCheckIn}>Check in hardware</button>
                        <button className="bg-amber-500 hover:bg-amber-700 text-white font-bold py-2 px-4 mx-2 rounded" onClick={handleCheckOut}>Check out hardware</button>
                    </div>
                </div>
          )}
          {modalContent === 'checkIn' && (
            <div>
              {/* CHECK IN HW CONTENT */}
              <h1 className="font-bold text-center block text-3xl">Check In Hardware</h1>
                <div className="pt-5">
                <FormControl>
                <FormLabel id="demo-row-radio-buttons-group-label">Hardware Type</FormLabel>
                <RadioGroup
                    row
                    name="row-radio-buttons-group"
                    value={selectedValue}
                    onChange={handleRadioChange}
                >
                    <FormControlLabel value="Computers" control={<Radio />} label="Computer" />
                    <FormControlLabel value="Servers" control={<Radio />} label="Server"/>
                </RadioGroup>
                </FormControl>
                </div>
                <div>
                    <label className="text-gray-500 block mt-3">Quantity</label>
                    <input className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100" type="text"
                    placeholder='Amount of hardware to check in'
                    style={{marginRight:'10px'}}
                    value={qty}
                    onChange={handleQty}
                    />
                </div>
                <div className="text-red-600 flex justify-center">{message}</div>
                <button type="button" className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-amber-600 to-red-400 hover:from-amber-700 hover:to-red-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg"onClick={(e) => handleConfirm(e)}>Confirm</button>
            </div>
          )}
          {modalContent === 'checkOut' && (
            <div>
              {/* CHECK OUT HW CONTENT */}
              <h1 className="font-bold text-center block text-3xl">Check Out Hardware</h1>
              <div className="pt-5">
                <FormControl>
                <FormLabel id="demo-row-radio-buttons-group-label">Hardware Type</FormLabel>
                <RadioGroup
                    row
                    name="row-radio-buttons-group"
                    value={selectedValue}
                    onChange={handleRadioChange}
                >
                    <FormControlLabel value="Computers" control={<Radio />} label="Computer" />
                    <FormControlLabel value="Servers" control={<Radio />} label="Server"/>
                </RadioGroup>
                </FormControl>
                </div>
              <div>
                    <label className="text-gray-500 block mt-3">Quantity</label>
                    <input className="rounded px-4 py-3 w-full mt-1 bg-white text-gray-900 border border-gray-200 focus:border-indigo-400 focus:outline-none focus:ring focus:ring-indigo-100" type="text"
                    placeholder='Amount of hardware to check out'
                    style={{marginRight:'10px'}}
                    value={qty}
                    onChange={handleQty}
                    />
                </div>
                <div className="text-red-600 flex justify-center">{message}</div>
                <button type="button" className="mt-6 transition transition-all block py-3 px-4 w-full text-white font-bold rounded cursor-pointer bg-gradient-to-r from-amber-600 to-red-400 hover:from-amber-700 hover:to-red-500 focus:bg-indigo-900 transform hover:-translate-y-1 hover:shadow-lg"onClick={(e) => handleConfirm(e)}>Confirm</button>
            </div>
          )}
        </form>
      </div>
    );
  }

function ManageResources({ isOpen, onRequestClose, project, fetchProjects, fetchResources }) {

    return (
        <Modal 
            isOpen={isOpen}
            onRequestClose={onRequestClose}
            className="justify-center overflow-x-hidden overflow-y-auto fixed items-center flex inset-0 z-50 outline-none focus:outline-none bg-gray-600 bg-opacity-75"
            ariaHideApp={false}
        >   
            <ManageResourcesContent 
                project = {project}
                onRequestClose={onRequestClose}
                fetchProjects={fetchProjects}
                fetchResources={fetchResources}
            />
        </Modal>
    );
}

export default ManageResources;