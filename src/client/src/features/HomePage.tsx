// features/HomePage.jsx
import './HomePage.css';

export function HomePage() {
    // placeholder data
    const categories = ['PTS', 'REB', 'AST', 'STL', 'BLK', '3PM', 'FG%', 'FT%'];

    const waiverTargets = [
        { name: 'Player A', team: 'MIA', note: 'Trending upward • strong 3PM' },
        { name: 'Player B', team: 'OKC', note: 'Good streamer for stocks' },
        { name: 'Player C', team: 'NYK', note: 'Reliable rebounds + efficiency' }
    ];

    const mySquad = ['Tyler Herro', 'Darius Garland', 'Steven Nguyen', 'Grayson Allen', 'Ajay Mitchell'];

    return (
        <div className='app'>
            {/* hero section */}
            <header className='hero'>
                <div>
                    <h1 className='logo'>WaiverWarrior</h1>
                    <p className='tagline'>Dominate the wire. Win the week.</p>
                    <p className='subtext'>
                        Your centralized hub for lineup decisions, category tracking, and waiver intel.
                    </p>

                    <div className='hero-buttons'>
                        <button className='btn primary' onClick={() => (window.location.href = '/dashboard')}>
                            Open Dashboard
                        </button>

                        <button className='btn ghost'>Add Matchup</button>
                    </div>
                </div>

                <div className='hero-card'>
                    <h2>This Week&apos;s Matchup</h2>
                    <p className='matchup-label'>Overview</p>

                    <div className='matchup-score'>
                        <div>
                            <span className='matchup-name'>You</span>
                            <span className='matchup-record'>5–3</span>
                        </div>
                        <div>
                            <span className='matchup-name enemy'>Opponent</span>
                            <span className='matchup-record'>3–5</span>
                        </div>
                    </div>

                    <p className='tiny-text'>
                        Target categories: <strong>FG%</strong>, <strong>AST</strong>, <strong>3PM</strong>,{' '}
                        <strong>STL</strong>.
                    </p>
                </div>
            </header>

            {/* categories */}
            <section className='section'>
                <h2>Category Snapshot</h2>
                <p className='section-sub'>A quick glance at the matchups you&apos;re aiming to control.</p>

                <div className='chips-row'>
                    {categories.map((cat) => (
                        <div key={cat} className='chip'>
                            <span className='chip-title'>{cat}</span>
                            <span className='chip-status'>in play</span>
                        </div>
                    ))}
                </div>
            </section>

            {/* waiver + roster */}
            <section className='section grid-2'>
                <div className='card'>
                    <div className='card-header'>
                        <h2>Waiver Targets</h2>
                        <span className='card-badge'>trending</span>
                    </div>
                    <p className='section-sub'>Players worth monitoring or adding based on recent performance.</p>

                    <ul className='list'>
                        {waiverTargets.map((p) => (
                            <li key={p.name} className='list-item'>
                                <div>
                                    <p className='list-title'>
                                        {p.name} <span className='list-team'>• {p.team}</span>
                                    </p>
                                    <p className='list-note'>{p.note}</p>
                                </div>
                                <button className='btn tiny'>Watch</button>
                            </li>
                        ))}
                    </ul>

                    <button className='btn fullwidth' onClick={() => (window.location.href = '/waiver')}>
                        View Full Waiver Board
                    </button>
                </div>

                <div className='card'>
                    <div className='card-header'>
                        <h2>My Squad</h2>
                        <span className='card-badge secondary'>overview</span>
                    </div>
                    <p className='section-sub'>Quick look at your roster.</p>

                    <ul className='list'>
                        {mySquad.map((name) => (
                            <li key={name} className='list-item'>
                                <p className='list-title'>{name}</p>
                                <p className='list-note light'>performance notes coming soon</p>
                            </li>
                        ))}
                    </ul>
                </div>
            </section>

            <footer className='footer'>
                <p>WaiverWarrior.</p>
            </footer>
        </div>
    );
}

export default HomePage;
