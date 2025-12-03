// features/HomePage.jsx
import { Card } from '@/components/Card';
import { Footer } from '@/components/Footer';
import { Hero } from '@/components/Hero';
import { Section } from '@/components/Section';
import { Matchup } from '@/features/Matchup';
import { Link } from '@tanstack/react-router';

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
        <>
            {/* hero section */}
            <Hero>
                <div>
                    <h1 className='logo'>WaiverWarrior</h1>
                    <p className='tagline'>Dominate the wire. Win the week.</p>
                    <p className='subtext'>
                        Your centralized hub for lineup decisions, category tracking, and waiver intel.
                    </p>

                    <div className='hero-buttons'>
                        <Link to='/dashboard'>
                            <button className='btn primary'>Open Dashboard</button>
                        </Link>
                        <button className='btn ghost'>Add Matchup</button>
                    </div>
                </div>

                <Matchup />
            </Hero>

            {/* categories */}
            <Section>
                <h2>Category Snapshot</h2>
                <Section.Sub>A quick glance at the matchups you're aiming to control.</Section.Sub>

                <div className='chips-row'>
                    {categories.map((cat) => (
                        <div key={cat} className='chip'>
                            <span className='chip-title'>{cat}</span>
                            <span className='chip-status'>in play</span>
                        </div>
                    ))}
                </div>
            </Section>

            {/* waiver + roster */}
            <Section className='grid-2'>
                <Card>
                    <Card.Header>
                        <h2>Waiver Targets</h2>
                        <Card.Badge>trending</Card.Badge>
                    </Card.Header>
                    <Section.Sub>Players worth monitoring or adding based on recent performance.</Section.Sub>

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

                    <Link to='/waiver'>
                        <button className='btn fullwidth'>View Full Waiver Board</button>
                    </Link>
                </Card>

                <Card>
                    <Card.Header>
                        <h2>My Squad</h2>
                        <Card.Badge className='secondary'>overview</Card.Badge>
                    </Card.Header>
                    <Section.Sub>Quick look at your roster.</Section.Sub>

                    <ul className='list'>
                        {mySquad.map((name) => (
                            <li key={name} className='list-item'>
                                <p className='list-title'>{name}</p>
                                <p className='list-note light'>performance notes coming soon</p>
                            </li>
                        ))}
                    </ul>
                </Card>
            </Section>

            <Footer>
                <p>WaiverWarrior.</p>
            </Footer>
        </>
    );
}

export default HomePage;
