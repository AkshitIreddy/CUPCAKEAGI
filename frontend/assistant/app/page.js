import Chat from "./components/chat";
import Navbar from "./components/nav";

export default function Home() {
  return (
    <>
      <div>
        <div className="navbar">
          <Navbar />
        </div>
        <div className="chat">
          <Chat />
        </div>
      </div>
    </>
  );
}
