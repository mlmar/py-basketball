// features/WaiverBoard.jsx
import { useState } from 'react';
import './HomePage.less';

export function WaiverBoard() {
    // simple mock data for now – this will be replaced by backend data later
    const waiverList = [
        {
            name: 'Player A',
            team: 'MIA',
            role: '3PM / scoring wing',
            positions: ['SG', 'SF'],
            cats: ['3PM', 'PTS', 'FG%']
        },
        {
            name: 'Player B',
            team: 'OKC',
            role: 'stocks streamer (STL + BLK)',
            positions: ['SG'],
            cats: ['STL', 'BLK']
        },
        {
            name: 'Player C',
            team: 'NYK',
            role: 'boards + FG% big',
            positions: ['PF', 'C'],
            cats: ['REB', 'FG%']
        },
        {
            name: 'Player D',
            team: 'MEM',
            role: 'points + assists guard',
            positions: ['PG'],
            cats: ['PTS', 'AST']
        },
        {
            name: 'Player E',
            team: 'SAC',
            role: '3PM + points, low TOs',
            positions: ['SG'],
            cats: ['3PM', 'PTS', 'TO']
        }
    ];

    const [activePos, setActivePos] = useState('ALL');
    const [activeCat, setActiveCat] = useState('ALL');

    const positionOptions = ['ALL', 'PG', 'SG', 'SF', 'PF', 'C', 'G', 'F'];
    const categoryOptions = ['ALL', 'FG%', 'FT%', '3PM', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TO'];

    const filteredWaivers = waiverList.filter((p) => {
        const posMatch = activePos === 'ALL' || p.positions?.includes(activePos as never);
        const catMatch = activeCat === 'ALL' || p.cats?.includes(activeCat as never);
        return posMatch && catMatch;
    });

    // trending area – mock data + trend filters
    const trendFilters = [
        { label: 'All', value: 'ALL' },
        { label: '+ Minutes', value: 'minutes_up' },
        { label: 'Usage bump', value: 'usage' },
        { label: 'Injury fill-in', value: 'injury' },
        { label: 'Hot stocks (STL/BLK)', value: 'stocks' }
    ];

    const [activeTrend, setActiveTrend] = useState('ALL');

    const trendingPlayers = [
        {
            name: 'Player F',
            team: 'LAL',
            note: 'Last 3: 22 PTS, 4 REB, 3.7 3PM',
            tags: ['minutes_up', 'usage']
        },
        {
            name: 'Player G',
            team: 'ORL',
            note: 'Stuffing stocks: 2.2 STL, 1.5 BLK recently',
            tags: ['stocks']
        },
        {
            name: 'Player H',
            team: 'CHI',
            note: 'Efficient big: 64% FG, solid boards',
            tags: ['minutes_up']
        },
        {
            name: 'Player I',
            team: 'DAL',
            note: 'Injury replacement getting starter run',
            tags: ['injury', 'minutes_up']
        }
    ];

    const filteredTrending =
        activeTrend === 'ALL' ? trendingPlayers : trendingPlayers.filter((p) => p.tags.includes(activeTrend));

    return (
        <div className='app'>
            {/* top bar */}
            <header className='section'>
                <div style={{ display: 'flex', justifyContent: 'space-between', gap: 12 }}>
                    <button className='btn tiny' onClick={() => (window.location.href = '/')}>
                        ← Home
                    </button>
                    <span className='tiny-text'>Waiver board – placeholder build</span>
                </div>

                <h1 className='logo'>WaiverWarrior</h1>
                <p className='tagline'>Full Waiver Board</p>
                <p className='subtext'>Big-picture view of possible adds. I&apos;ll hook this into live data later.</p>
            </header>

            {/* main waiver board */}
            <section className='section'>
                <div className='card waiver-card'>
                    <div className='card-header'>
                        <h2>All Waiver Targets (mock)</h2>
                        <span className='card-badge'>early version</span>
                    </div>
                    <p className='section-sub'>
                        Right now this is just hardcoded. Plan is to swap this for real backend results and add proper
                        filters (team, position, categories).
                    </p>

                    <div className='filter-block'>
                        {/* positions */}
                        <div className='filter-row-line'>
                            <span className='filter-label'>Positions</span>
                            <div className='filter-pill-row'>
                                {positionOptions.map((pos) => (
                                    <button
                                        key={pos}
                                        className={'filter-pill' + (activePos === pos ? ' filter-pill-active' : '')}
                                        onClick={() => setActivePos(pos)}
                                    >
                                        {pos}
                                    </button>
                                ))}
                            </div>
                        </div>

                        {/* categories */}
                        <div className='filter-row-line'>
                            <span className='filter-label'>Categories</span>
                            <div className='filter-pill-row'>
                                {categoryOptions.map((cat) => (
                                    <button
                                        key={cat}
                                        className={'filter-pill' + (activeCat === cat ? ' filter-pill-active' : '')}
                                        onClick={() => setActiveCat(cat)}
                                    >
                                        {cat}
                                    </button>
                                ))}
                            </div>
                        </div>
                    </div>

                    <ul className='list'>
                        {filteredWaivers.map((p) => (
                            <li key={p.name} className='list-item'>
                                <div>
                                    <p className='list-title'>
                                        {p.name} <span className='list-team'>• {p.team}</span>
                                    </p>
                                    <p className='list-note'>{p.role}</p>
                                </div>
                                <button className='btn tiny'>Shortlist</button>
                            </li>
                        ))}
                    </ul>
                </div>
            </section>

            {/* trending section */}
            <section className='section'>
                <div className='card trending-card'>
                    <div className='card-header'>
                        <h2>Trending Players (mock)</h2>
                        <span className='card-badge trending-badge'>trending</span>
                    </div>
                    <p className='section-sub'>
                        Quick look at players on a heater. Eventually this will pull from recent game logs and your
                        league settings.
                    </p>

                    <div className='filter-block trending-filter-row'>
                        <div className='filter-row-line'>
                            <span className='filter-label'>Trending filters</span>
                            <div className='filter-pill-row'>
                                {trendFilters.map((f) => (
                                    <button
                                        key={f.value}
                                        className={
                                            'filter-pill' + (activeTrend === f.value ? ' filter-pill-active-trend' : '')
                                        }
                                        onClick={() => setActiveTrend(f.value)}
                                    >
                                        {f.label}
                                    </button>
                                ))}
                            </div>
                        </div>
                    </div>

                    <ul className='list'>
                        {filteredTrending.map((p) => (
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
                </div>
            </section>

            <footer className='footer'>
                <p>WaiverWarrior · full board mock v0.1</p>
            </footer>
        </div>
    );
}
