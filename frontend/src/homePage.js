import React from 'react';
import { useState } from 'react';
import { useNavigate } from "react-router";

function HomePage() {
    return (
        
        <div className="container mx-auto py-32">
        <div className="flex">
          
          <div className="w-1/5 bg-blue-300 h-128 p-4 mr-10 ml-4 items-center">
            <p>This is the left box</p>
          </div>
  
          <div className="w-3/4 bg-green-300 h-128 p-4">
            <p>This is the middle box</p>
          </div>
        </div>
      </div>
    );
}

export default HomePage;
