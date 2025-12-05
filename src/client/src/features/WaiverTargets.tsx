import { Card } from '@/components/Card';
import type { ContainerProps } from '@/components/types/ContainerProps';
import { useIsLoggedIn } from '@/hooks/useIsLoggedIn';
import { Link } from '@tanstack/react-router';

const waiverTargets = [
    { name: 'Player A', team: 'MIA', note: 'Trending upward • strong 3PM' },
    { name: 'Player B', team: 'OKC', note: 'Good streamer for stocks' },
    { name: 'Player C', team: 'NYK', note: 'Reliable rebounds + efficiency' }
];

export function WaiverTargets(props: ContainerProps) {
    const isLoggedIn = useIsLoggedIn();

    return (
        <Card {...props}>
            <Card.Header>
                <h2>Waiver Targets</h2>
                <Card.Badge>trending</Card.Badge>
            </Card.Header>
            <Card.Sub>Players worth monitoring or adding based on recent performance.</Card.Sub>

            <ul className='list'>
                {waiverTargets.map((p) => (
                    <li key={p.name} className='list-item'>
                        <div>
                            <p className='list-title'>
                                {p.name} <span className='list-team'>• {p.team}</span>
                            </p>
                            <p className='list-note'>{p.note}</p>
                        </div>
                        {isLoggedIn && (
                            <button className='btn tiny' onClick={() => alert('TODO')}>
                                Watch
                            </button>
                        )}
                    </li>
                ))}
            </ul>

            <Link to='/waiver'>
                <button className='btn fullwidth'>View Full Waiver Board</button>
            </Link>
        </Card>
    );
}
