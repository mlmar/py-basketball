// features/WaiverBoard.jsx
import { BackButton } from '@/components/BackButton';
import { Card } from '@/components/Card';
import { Footer } from '@/components/Footer';
import { Header } from '@/components/Header';
import { Section } from '@/components/Section';
import { TrendingPlayers } from '@/features/TrendingPlayers';
import { useState } from 'react';

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

    return (
        <>
            {/* top bar */}
            <Header className='section'>
                <Header.TopNav>
                    <BackButton>Home</BackButton>
                    <span className='tiny-text'>Waiver board – placeholder build</span>
                </Header.TopNav>

                <Header.Logo>WaiverWarrior</Header.Logo>
                <Header.Tagline>Full Waiver Board</Header.Tagline>
                <Header.Subtext>Big-picture view of possible adds. I'll hook this into live data later.</Header.Subtext>
            </Header>

            {/* main waiver board */}
            <Section>
                <Card className='waiver-card'>
                    <Card.Header>
                        <h2>All Waiver Targets (mock)</h2>
                        <Card.Badge>early version</Card.Badge>
                    </Card.Header>
                    <Card.Sub>
                        Right now this is just hardcoded. Plan is to swap this for real backend results and add proper
                        filters (team, position, categories).
                    </Card.Sub>

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
                </Card>
            </Section>

            {/* trending section */}
            <TrendingPlayers limit={5} />

            <Footer>
                <p>WaiverWarrior · full board mock v0.1</p>
            </Footer>
        </>
    );
}
