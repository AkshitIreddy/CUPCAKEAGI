import "./globals.css";
import Navbar from "./components/nav";
import { Crimson_Text } from "next/font/google";

const crimson = Crimson_Text({
  weight: "400",
  subsets: ["latin"],
  display: "swap",
});

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="scroller back">
        <div className={`${crimson.className} back h-full`}>{children}</div>
      </body>
    </html>
  );
}
