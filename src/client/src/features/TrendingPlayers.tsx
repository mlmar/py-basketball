import { Card } from '@/components/Card';
import { Section } from '@/components/Section';
import { useTrendingFilter } from '@/hooks/useActiveTrend';
import { useTrendingplayers } from '@/hooks/useTrendingPlayers';
import type { ProjectedPlayer } from '@/services/types/ProjectedPlayer';
import { Link } from '@tanstack/react-router';

/**
 * Placeholder data
 */
// trending area – mock data + trend filters
const trendFilters = [
    { label: 'All', value: null },
    { label: '+ Minutes', value: 'minutes_up' },
    // { label: 'Usage bump', value: 'usage' },
    // { label: 'Injury fill-in', value: 'injury' },
    { label: 'Hot stocks (STL/BLK)', value: 'stocks' }
];

// Prop type
type TrendingPlayersProps = {
    limit: number;
};

/**
 * Renders list of trending players from backend service (placeholder data for now)
 * @returns
 */
export function TrendingPlayers({ limit }: TrendingPlayersProps) {
    const [trendingFilter, setTrendingFilter] = useTrendingFilter();
    const { data, isLoading, isAllData } = useTrendingplayers(trendingFilter, limit);

    return (
        <Section>
            <Card className='trending-card'>
                <Card.Header>
                    <h2>Trending Players</h2>
                    <Card.Badge className='trending-badge'>trending</Card.Badge>
                </Card.Header>
                <Card.Sub>Quick look at players on a heater.</Card.Sub>

                <div className='filter-block trending-filter-row'>
                    <div className='filter-row-line'>
                        <span className='filter-label'>Trending filters</span>
                        <div className='filter-pill-row'>
                            {trendFilters.map((f) => (
                                <button
                                    key={f.value}
                                    className={
                                        'filter-pill' + (trendingFilter === f.value ? ' filter-pill-active-trend' : '')
                                    }
                                    onClick={() => setTrendingFilter(f.value)}
                                >
                                    {f.label}
                                </button>
                            ))}
                        </div>
                    </div>
                </div>

                <ul className='list'>
                    {isLoading && 'Trending players are loading'}
                    {data.map((projectedPlayer) => {
                        return (
                            <li className='list-item' key={projectedPlayer.player.player}>
                                <section>
                                    <p className='list-note'> {projectedPlayer.player.player} </p>
                                    <p className='list-title'> {projectedPlayer.analysis} </p>
                                </section>
                                <button className='btn tiny' onClick={() => alert('TODO')}>
                                    Watch
                                </button>
                            </li>
                        );
                    })}
                </ul>
                {!isAllData && (
                    <Link to='/trending'>
                        <button className='btn fullwidth'>View Full Trending List</button>
                    </Link>
                )}
            </Card>
        </Section>
    );
}

type ProjectedPlayerItemProps = {
    projectedPlayer: ProjectedPlayer;
};

export function ProjectedPlayerItem({ projectedPlayer }: ProjectedPlayerItemProps) {
    <li>
        <details>
            <p className='list-note'> {projectedPlayer.player.player} </p>
            <p className='list-title'> {projectedPlayer.analysis} </p>
        </details>
    </li>;
}
