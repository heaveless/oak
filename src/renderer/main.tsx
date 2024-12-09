import "./styles/global.css";

import { createRoot } from "react-dom/client";
// import { BrowserRouter as Router, Routes } from "react-router";
import { MainPage } from "./pages";

const root = createRoot(document.body);
root.render(<MainPage />);
