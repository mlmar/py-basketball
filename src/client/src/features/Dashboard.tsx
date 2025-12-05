import { BackButton } from '@/components/BackButton';
import { Card } from '@/components/Card';
import { Header } from '@/components/Header';
import { Section } from '@/components/Section';
import { Link } from '@tanstack/react-router';

// features/Dashboard.jsx
export function Dashboard() {
    // rough waiver board data until this is wired to the backend
    const waiverBoard = [
        {
            name: 'Player A',
            team: 'MIA',
            role: '3PM / scoring',
            note: 'Hot from deep last few games.'
        },
        {
            name: 'Player B',
            team: 'OKC',
            role: 'stocks',
            note: 'Nice steals + blocks streamer.'
        },
        {
            name: 'Player C',
            team: 'NYK',
            role: 'boards',
            note: 'Solid rebounds without killing FG%.'
        },
        {
            name: 'Player D',
            team: 'SAC',
            role: 'assists',
            note: 'Low-end PG for dimes when I need them.'
        }
    ];

    return (
        <>
            {/* top section */}
            <Header>
                <Header.TopNav>
                    <BackButton>Home</BackButton>
                </Header.TopNav>
                <Header.Logo>WaiverWarrior</Header.Logo>
                <Header.Tagline>Dashboard (early build)</Header.Tagline>
                <Header.Subtext>
                    Spot where I'm going to plug in live stats, matchup tracking, and AI calls from the backend.
                </Header.Subtext>
            </Header>

            {/* main grid */}
            <Section className='grid-2'>
                <Card>
                    <Card.Header>
                        <h2>Today's Games</h2>
                        <span className='card-badge'>schedule</span>
                    </Card.Header>
                    <Card.Sub>This card will pull in upcoming games once the API is hooked up.</Card.Sub>
                </Card>

                <Card>
                    <Card.Header>
                        <h2>Category Tracker</h2>
                        <Card.Badge className='secondary'>beta</Card.Badge>
                    </Card.Header>
                    <Card.Sub>Placeholder for charts showing how my team is doing in each cat.</Card.Sub>
                </Card>
            </Section>

            {/* waiver board preview */}
            <Section>
                <Card>
                    <Card.Header>
                        <h2>Waiver Board</h2>
                        <Card.Badge>my notes</Card.Badge>
                    </Card.Header>
                    <Card.Sub>
                        Early version of my waiver list. I'll swap this out for real data once the backend is plugged
                        in.
                    </Card.Sub>

                    <ul className='list'>
                        {waiverBoard.map((p) => (
                            <li key={p.name} className='list-item'>
                                <div>
                                    <p className='list-title'>
                                        {p.name} <span className='list-team'>• {p.team}</span>
                                    </p>
                                    <p className='list-note'>{p.note}</p>
                                </div>
                                <span className='pill soft'>{p.role}</span>
                            </li>
                        ))}
                    </ul>

                    <Link to='/waiver'>
                        <button className='btn fullwidth'>Open Full Waiver Board</button>
                    </Link>
                </Card>
            </Section>
        </>
    );
}
