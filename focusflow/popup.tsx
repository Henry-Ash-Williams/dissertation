import { useState } from "react"
import "popup.css";
import React from "react";

function IndexPopup() {
  return (
    <div
      style={{
        width: '200px',
        margin: '0 auto', // Center align the component
        display: "flex",
        flexDirection: "column",
        alignItems: "center", // Center align the items inside
        padding: 16,
        fontFamily: "'Montserrat', sans-serif",
        backgroundColor: '#313244',
        color: "#CDD6F4",
        border: "0",
      }}>
        <svg width="96" height="96" viewBox="0 0 96 96" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="96" height="96" fill="#313244"/>
          <circle cx="48" cy="48" r="42" fill="url(#paint0_linear_1_11)"/>
          <path d="M30.48 65H23.04C22.432 65 21.984 64.872 21.696 64.616C21.44 64.328 21.312 63.88 21.312 63.272V32.168C21.312 31.56 21.44 31.128 21.696 30.872C21.984 30.584 22.432 30.44 23.04 30.44H44.448C45.056 30.44 45.488 30.584 45.744 30.872C46.032 31.128 46.176 31.56 46.176 32.168V37.88C46.176 38.488 46.032 38.936 45.744 39.224C45.488 39.48 45.056 39.608 44.448 39.608H32.208V44.6H40.56C41.168 44.6 41.6 44.744 41.856 45.032C42.144 45.288 42.288 45.72 42.288 46.328V52.088C42.288 52.696 42.144 53.144 41.856 53.432C41.6 53.688 41.168 53.816 40.56 53.816H32.208V63.272C32.208 63.88 32.064 64.328 31.776 64.616C31.52 64.872 31.088 65 30.48 65ZM60.1519 65H52.7119C52.1039 65 51.6559 64.872 51.3679 64.616C51.1119 64.328 50.9839 63.88 50.9839 63.272V32.168C50.9839 31.56 51.1119 31.128 51.3679 30.872C51.6559 30.584 52.1039 30.44 52.7119 30.44H74.1199C74.7279 30.44 75.1599 30.584 75.4159 30.872C75.7039 31.128 75.8479 31.56 75.8479 32.168V37.88C75.8479 38.488 75.7039 38.936 75.4159 39.224C75.1599 39.48 74.7279 39.608 74.1199 39.608H61.8799V44.6H70.2319C70.8399 44.6 71.2719 44.744 71.5279 45.032C71.8159 45.288 71.9599 45.72 71.9599 46.328V52.088C71.9599 52.696 71.8159 53.144 71.5279 53.432C71.2719 53.688 70.8399 53.816 70.2319 53.816H61.8799V63.272C61.8799 63.88 61.7359 64.328 61.4479 64.616C61.1919 64.872 60.7599 65 60.1519 65Z" fill="white"/>
          <defs>
          <linearGradient id="paint0_linear_1_11" x1="6" y1="90" x2="90" y2="6" gradientUnits="userSpaceOnUse">
            <stop stop-color="#74C7EC"/>
            <stop offset="1" stop-color="#CBA6F7"/>
          </linearGradient>
          </defs>
        </svg>
        <h1>FocusFlow</h1>
        <p>Enabled on this page</p>
      </div>
  )
}

export default IndexPopup
