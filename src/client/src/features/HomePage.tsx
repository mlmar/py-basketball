// features/HomePage.jsx
import { Card } from '@/components/Card';
import { Hero } from '@/components/Hero';
import { LoginButton } from '@/components/LoginButton';
import { LogoutButton } from '@/components/LogoutButton';
import { Section } from '@/components/Section';
import { Matchup } from '@/features/Matchup';
import { TrendingPlayers } from '@/features/TrendingPlayers';
import { WaiverTargets } from '@/features/WaiverTargets';
import { useIsLoggedIn } from '@/hooks/useIsLoggedIn';
import { Link } from '@tanstack/react-router';

export function HomePage() {
    // placeholder data
    const isLoggedIn = useIsLoggedIn();
    const categories = ['PTS', 'REB', 'AST', 'STL', 'BLK', '3PM', 'FG%', 'FT%'];
    const mySquad = ['Tyler Herro', 'Darius Garland', 'Steven Nguyen', 'Grayson Allen', 'Ajay Mitchell'];

    return (
        <>
            {/* hero section */}
            <Hero>
                <div>
                    <h1 className='logo'>WaiverWarrior (Mock)</h1>
                    <p className='tagline'>Dominate the wire. Win the week.</p>
                    <p className='subtext'>
                        Your centralized hub for lineup decisions, category tracking, and waiver intel.
                    </p>

                    <div className='hero-buttons'>
                        {!isLoggedIn && <LoginButton />}
                        {isLoggedIn && <LogoutButton />}
                        <Link to='/dashboard'>
                            <button className='btn primary'>Open Dashboard</button>
                        </Link>
                        <button className='btn ghost'>Add Matchup</button>
                    </div>
                </div>

                <Matchup />
            </Hero>

            <TrendingPlayers limit={5} />

            {/* categories */}
            <Section>
                <h2>Category Snapshot (Mock)</h2>
                <Card.Sub>A quick glance at the matchups you're aiming to control.</Card.Sub>

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
                <WaiverTargets />

                <Card>
                    <Card.Header>
                        <h2>My Squad (Mock)</h2>
                        <Card.Badge className='secondary'>overview</Card.Badge>
                    </Card.Header>
                    <Card.Sub>Quick look at your roster.</Card.Sub>

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
        </>
    );
}

export default HomePage;
