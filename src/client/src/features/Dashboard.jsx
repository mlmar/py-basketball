// src/features/WaiverBoard.jsx
import { useState } from "react";
import "./HomePage.css";
import { Link } from "@tanstack/react-router";

const ALL_ROLES_FILTERS = ["ALL","PTS", "FG%", "FTS", "3PM", "stocks", "boards", "assists","TOs"];

const TRENDING_FILTERS = [
  "ALL",
  "Hot",
  "Cold",
  "+ Minutes",
  "- Minutes",
  "Injuries",
];

export function WaiverBoard() {
  // dummy data for now – I’ll swap this out for real backend stats later
  const waiverList = [
    { name: "Player A", team: "MIA", role: "3PM / scoring wing" },
    { name: "Player B", team: "OKC", role: "stocks streamer (STL + BLK)" },
    { name: "Player C", team: "NYK", role: "boards + FG% big" },
    { name: "Player D", team: "MEM", role: "points + assists guard" },
    { name: "Player E", team: "SAC", role: "3PM + points, low TOs" },
  ];

  const trendingPlayers = [
    {
      name: "Player F",
      team: "ORL",
      tag: "Hot",
      note: "Minutes and usage both climbing.",
    },
    {
      name: "Player G",
      team: "CHI",
      tag: "Cold",
      note: "Shot volume same but shots not falling.",
    },
    {
      name: "Player H",
      team: "NOP",
      tag: "+ Minutes",
      note: "Moved into starting lineup last 3 games.",
    },
    {
      name: "Player I",
      team: "DEN",
      tag: "- Minutes",
      note: "Losing run with second unit.",
    },
    {
      name: "Player J",
      team: "PHX",
      tag: "Injuries",
      note: "Getting a bump while starter is out.",
    },
  ];

  // simple filters so I can quickly sort by what I’m looking for
  const [activeRoleFilter, setActiveRoleFilter] = useState("ALL");
  const [activeTrendFilter, setActiveTrendFilter] = useState("ALL");

  const filteredWaiverList = waiverList.filter((p) =>
    activeRoleFilter === "ALL"
      ? true
      : p.role.toLowerCase().includes(activeRoleFilter.toLowerCase())
  );

  const filteredTrending = trendingPlayers.filter((p) =>
    activeTrendFilter === "ALL"
      ? true
      : p.tag.toLowerCase().includes(activeTrendFilter.toLowerCase())
  );

  return (
    <div className="app">
      {/* top bar */}
      <header className="section">
        <div
          style={{ display: "flex", justifyContent: "space-between", gap: 12 }}
        >
          <Link to="/" className="btn tiny">
            ← Home
          </Link>
          <span className="tiny-text">Waiver board – placeholder build</span>
        </div>

        <h1 className="logo">WaiverWarrior</h1>
        <p className="tagline">Full Waiver Board</p>
        <p className="subtext">
          Big-picture view of possible adds. I’ll hook this into live data
          later.
        </p>
      </header>

      {/* main grid: all targets + trending box */}
      <section className="section grid-2">
        {/* All Waiver Targets */}
        <div className="card" style={{ borderColor: "rgba(37, 99, 235, 0.7)" }}>
          <div className="card-header">
            <h2>All Waiver Targets (mock)</h2>
            <span className="card-badge">early version</span>
          </div>
          <p className="section-sub">
            Right now this is just hardcoded. Goal is to swap it with real
            backend results and filters (team, position, categories).
          </p>

          {/* role filter row */}
          <div className="chips-row filter-row">
            {ALL_ROLES_FILTERS.map((label) => (
              <button
                key={label}
                className={
                  "filter-pill" +
                  (activeRoleFilter === label ? " filter-pill-active" : "")
                }
                onClick={() => setActiveRoleFilter(label)}
              >
                {label === "ALL" ? "All roles" : label}
              </button>
            ))}
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

        {/* Trending section */}
        <div className="card trending-card">
          <div className="card-header">
            <h2>Trending Players</h2>
            <span className="card-badge trending-badge">trending filters</span>
          </div>
          <p className="section-sub">
            Quick scan for hot, cold, and injury-boost guys. For now this is
            all mock data.
          </p>

          {/* trending filters */}
          <div className="filter-block trending-filter-row">
            <p className="filter-label">Trending filters</p>
            <div className="filter-pill-row">
              {TRENDING_FILTERS.map((label) => (
                <button
                  key={label}
                  className={
                    "filter-pill" +
                    (activeTrendFilter === label
                      ? " filter-pill-active-trend"
                      : "")
                  }
                  onClick={() => setActiveTrendFilter(label)}
                >
                  {label}
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
                  <p className="list-note">{p.note}</p>
                </div>
                <span className="pill soft">{p.tag}</span>
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
