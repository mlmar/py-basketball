// src/pages/WaiverBoard.jsx
import { useState } from "react";
import "../App.css";

function WaiverBoard() {
  // --- mock data for the main waiver board ---
  const waiverList = [
    {
      name: "Player A",
      team: "MIA",
      role: "3PM / scoring wing",
      pos: ["SG", "SF"],
      cats: ["3PM", "PTS"],
    },
    {
      name: "Player B",
      team: "OKC",
      role: "stocks streamer (STL + BLK)",
      pos: ["PG"],
      cats: ["STL", "BLK"],
    },
    {
      name: "Player C",
      team: "NYK",
      role: "boards + FG% big",
      pos: ["PF", "C"],
      cats: ["REB", "FG%"],
    },
    {
      name: "Player D",
      team: "MEM",
      role: "points + assists guard",
      pos: ["PG"],
      cats: ["PTS", "AST"],
    },
    {
      name: "Player E",
      team: "SAC",
      role: "3PM + points, low TOs",
      pos: ["SG"],
      cats: ["3PM", "PTS", "TO"],
    },
  ];

  const positionOptions = ["ALL", "PG", "SG", "SF", "PF", "C", "G", "F"];
  const categoryOptions = [
    "ALL",
    "FG%",
    "FT%",
    "3PM",
    "PTS",
    "REB",
    "AST",
    "STL",
    "BLK",
    "TO",
  ];

  const [posFilter, setPosFilter] = useState("ALL");
  const [catFilter, setCatFilter] = useState("ALL");

  const filteredWaiverList = waiverList.filter((p) => {
    const matchesPos =
      posFilter === "ALL" || p.pos.includes(posFilter) || // G/F as catch-all
      (posFilter === "G" && (p.pos.includes("PG") || p.pos.includes("SG"))) ||
      (posFilter === "F" && (p.pos.includes("SF") || p.pos.includes("PF")));
    const matchesCat = catFilter === "ALL" || p.cats.includes(catFilter);
    return matchesPos && matchesCat;
  });

  // --- mock data for trending section ---
  const trendingFilters = [
    { id: "ALL", label: "All" },
    { id: "SCORING", label: "Scoring heater" },
    { id: "MINUTES", label: "Minutes +/-" },
    { id: "INJURY", label: "Injury fill-in" },
    { id: "USAGE", label: "Usage bump" },
    { id: "STOCKS", label: "Stocks run" },
    { id: "3PM", label: "+3PM" },
    { id: "EFFICIENCY", label: "Efficient" },

  ];

  const [activeTrendingFilter, setActiveTrendingFilter] = useState("ALL");

  const trendingPlayers = [
    {
      name: "Player F",
      team: "LAL",
      blurb: "Last 3: 22 PTS, 4 REB, 3.7 3PM in 30+ minutes.",
      tags: ["SCORING", "MINUTES", "USAGE", "3PM"],
    },
    {
      name: "Player G",
      team: "ORL",
      blurb: "Stuffing stocks: 2.2 STL, 1.5 BLK recently.",
      tags: ["STOCKS", "USAGE"],
    },
    {
      name: "Player H",
      team: "CHI",
      blurb: "Efficient big: 64% FG, solid boards, minutes creeping up.",
      tags: ["MINUTES", "USAGE", "EFFICIENCY"],
    },
    {
      name: "Player I",
      team: "DAL",
      blurb: "Injury fill-in logging starter minutes at guard.",
      tags: ["INJURY", "MINUTES", "USAGE"],
    },
  ];

  const filteredTrending = trendingPlayers.filter((p) =>
    activeTrendingFilter === "ALL"
      ? true
      : p.tags.includes(activeTrendingFilter)
  );

  return (
    <div className="app">
      {/* top bar */}
      <header className="section">
        <div style={{ display: "flex", justifyContent: "space-between", gap: 12 }}>
          <button
            className="btn tiny"
            onClick={() => (window.location.href = "/")}
          >
            ← Home
          </button>
          <span className="tiny-text">Waiver board – placeholder build</span>
        </div>

        <h1 className="logo">WaiverWarrior</h1>
        <p className="tagline">Full Waiver Board</p>
        <p className="subtext">
          Big-picture view of possible adds. I’ll hook this into live data
          later.
        </p>
      </header>

      {/* --- All Waiver Targets --- */}
      <section className="section">
        <div className="card">
          <div className="card-header">
            <h2>All Waiver Targets (mock)</h2>
            <span className="card-badge">early version</span>
          </div>
          <p className="section-sub">
            Right now this is just hardcoded. Plan is to swap this for real
            backend results and add proper filters (team, position, categories).
          </p>

          {/* position + category filters */}
          <div className="filter-block">
            <div className="filter-row-line">
              <span className="filter-label">Positions</span>
              <div className="filter-pill-row">
                {positionOptions.map((pos) => (
                  <button
                    key={pos}
                    className={
                      "filter-pill" +
                      (posFilter === pos ? " filter-pill-active" : "")
                    }
                    onClick={() => setPosFilter(pos)}
                  >
                    {pos}
                  </button>
                ))}
              </div>
            </div>

            <div className="filter-row-line">
              <span className="filter-label">Categories</span>
              <div className="filter-pill-row">
                {categoryOptions.map((cat) => (
                  <button
                    key={cat}
                    className={
                      "filter-pill" +
                      (catFilter === cat ? " filter-pill-active" : "")
                    }
                    onClick={() => setCatFilter(cat)}
                  >
                    {cat}
                  </button>
                ))}
              </div>
            </div>
          </div>

          <ul className="list">
            {filteredWaiverList.map((p) => (
              <li key={p.name} className="list-item">
                <div>
                  <p className="list-title">
                    {p.name} <span className="list-team">• {p.team}</span>
                  </p>
                  <p className="list-note">{p.role}</p>
                </div>
                <button className="btn tiny">Shortlist</button>
              </li>
            ))}
          </ul>
        </div>
      </section>

      {/* --- Trending Players --- */}
      <section className="section">
        <div className="card trending-card">
          <div className="card-header">
            <h2>Trending Players (mock)</h2>
            <span className="card-badge trending-badge">trending</span>
          </div>
          <p className="section-sub">
            Quick look at players on a heater. Eventually this will come from
            recent game logs + your league settings.
          </p>

          <div className="filter-block trending-filter-row">
            <div className="filter-pill-row">
              {trendingFilters.map((f) => (
                <button
                  key={f.id}
                  className={
                    "filter-pill" +
                    (activeTrendingFilter === f.id
                      ? " filter-pill-active-trend"
                      : "")
                  }
                  onClick={() => setActiveTrendingFilter(f.id)}
                >
                  {f.label}
                </button>
              ))}
            </div>
          </div>

          <ul className="list">
            {filteredTrending.map((p) => (
              <li key={p.name} className="list-item">
                <div>
                  <p className="list-title">
                    {p.name} <span className="list-team">• {p.team}</span>
                  </p>
                  <p className="list-note">{p.blurb}</p>
                </div>
                <button className="btn tiny">Watch</button>
              </li>
            ))}
          </ul>
        </div>
      </section>

      <footer className="footer">
        <p>WaiverWarrior · full board mock v0.1</p>
      </footer>
    </div>
  );
}

export default WaiverBoard;
