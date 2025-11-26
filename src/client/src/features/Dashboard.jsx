import "../App.css";
import { Link } from "react-router-dom";

function Dashboard() {
  // rough waiver board data until I hook this up to the backend
  const waiverBoard = [
    { name: "Player A", team: "MIA", role: "3PM / scoring", note: "Hot from deep last few games." },
    { name: "Player B", team: "OKC", role: "stocks", note: "Nice steals + blocks streamer." },
    { name: "Player C", team: "NYK", role: "boards", note: "Solid rebounds without killing FG%." },
    { name: "Player D", team: "SAC", role: "assists", note: "Low-end PG for dimes when I need them." },
  ];

  return (
    <div className="app">
      {/* simple top nav so I can bounce back to the homepage */}
      <nav className="top-nav">
        <Link to="/" className="home-link">
          ← Back to home
        </Link>
      </nav>

      {/* top section */}
      <header className="section">
        <h1 className="logo">WaiverWarrior</h1>
        <p className="tagline">Dashboard (early build)</p>
        <p className="subtext">
          Spot where I’m going to plug in live stats, matchup tracking, and AI
          calls from the backend.
        </p>
      </header>

      {/* main grid */}
      <section className="section grid-2">
        <div className="card">
          <div className="card-header">
            <h2>Today&apos;s Games</h2>
            <span className="card-badge">schedule</span>
          </div>
          <p className="section-sub">
            This card will pull in upcoming games once I hook the API up.
          </p>
        </div>

        <div className="card">
          <div className="card-header">
            <h2>Category Tracker</h2>
            <span className="card-badge secondary">beta</span>
          </div>
          <p className="section-sub">
            Placeholder for charts showing how my team is doing in each cat.
          </p>
        </div>
      </section>

      {/* waiver board section */}
      <section className="section">
  <div className="card">
    <div className="card-header">
      <h2>Waiver Board</h2>
      <span className="card-badge">my notes</span>
    </div>

    <p className="section-sub">
      Early version of my waiver list. I’ll swap this out for real data once the backend is plugged in.
    </p>

    <ul className="list">
      {waiverBoard.map((p) => (
        <li key={p.name} className="list-item">
          <div>
            <p className="list-title">
              {p.name} <span className="list-team">• {p.team}</span>
            </p>
            <p className="list-note">{p.note}</p>
          </div>
          <span className="pill soft">{p.role}</span>
        </li>
      ))}
    </ul>

    {/* button I added to open the full waiver board */}
    <button
      className="btn fullwidth"
      onClick={() => (window.location.href = "/waiver")}
    >
      View Full Waiver Board
    </button>
  </div>
</section>


      <footer className="footer">
        <p>WaiverWarrior · dashboard v0.1</p>
      </footer>
    </div>
  );
}

export default Dashboard;
