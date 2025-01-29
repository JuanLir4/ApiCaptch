// src/components/ui/card.js
import React from "react";

export const Card = ({ children, className }) => (
  <div className={`rounded-2xl shadow-lg bg-white ${className}`}>{children}</div>
);

export const CardContent = ({ children, className }) => (
  <div className={`p-4 ${className}`}>{children}</div>
);