import React from "react";
import Image from "next/image";
import sql from "./../assets/logo.png";

const Navbar = () => {
  return (
    <nav className={`glass flex items-center justify-between px-8 py-4 pb-6`}>
      <div className="flex items-center">
        <Image
          src={sql}
          alt="logo"
          className="mb-2 mr-2 h-12 w-10 rounded-xl"
        />
        <h1 className="gradtext mb-0 pb-0 text-3xl font-bold text-gray-600 hover:text-white">
          CUPCAKEAGI
        </h1>
      </div>
      <div className="flex items-center text-xl font-bold text-gray-600">
        <a href="#" className="mr-4  hover:text-white">
          Multisensory
        </a>
        <a href="#" className="mr-4  hover:text-white">
          Emotions
        </a>
        <a href="#" className="mr-4 hover:text-white">
          Persistent Memory
        </a>
        <a href="#" className="mr-4 hover:text-white">
          Random Thoughts & Dreams
        </a>
        <a href="#" className="mr-4 hover:text-white">
          Special Abilities
        </a>
        <a href="#" className="mr-4  hover:text-white">
          Assign & Schedule Tasks
        </a>
      </div>
    </nav>
  );
};

export default Navbar;
