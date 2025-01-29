// src/components/ui/button.js
import React from "react";

export const Button = ({ children, className, ...props }) => (
  <button
    className={`px-4 py-2 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 ${className}`}
    {...props}
  >
    {children}
  </button>
);
