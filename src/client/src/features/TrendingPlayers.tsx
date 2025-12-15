import { Card } from '@/components/Card';
import { Section } from '@/components/Section';
import { Spinner } from '@/components/Spinner';
import type { ContainerProps } from '@/components/types/ContainerProps';
import { useTrendingFilter } from '@/hooks/useActiveTrend';
import { useIsLoggedIn } from '@/hooks/useIsLoggedIn';
import { useTrendingplayers } from '@/hooks/useTrendingPlayers';
import type { TrendingPlayer } from '@/services/types/TrendingPlayer';
import { css } from '@/util/css';
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
interface TrendingPlayersProps extends ContainerProps {
    limit: number;
}

/**
 * Renders list of trending players from backend service (placeholder data for now)
 * @returns
 */
export function TrendingPlayers({ className, limit }: TrendingPlayersProps) {
    const isLoggedIn = useIsLoggedIn();
    const [trendingFilter, setTrendingFilter] = useTrendingFilter();
    const { data, isLoading } = useTrendingplayers(trendingFilter, limit);

    return (
        <Section className={css('trending-players', className)}>
            <Card className='trending-card'>
                <Card.Header>
                    <h2>Trending Players</h2>
                    <Card.Badge className='trending-badge'>trending</Card.Badge>
                </Card.Header>
                <Card.Sub>
                    Quick look at players on a heater.
                    {data.status === 'PROCESSING' && ' Processing new daily analysis - check back in a few minutes.'}
                </Card.Sub>

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

                {isLoading && <Spinner />}
                <ul className='list'>
                    {data.result.map((trendingPlayer) => {
                        return (
                            <TrendingPlayerItem
                                trendingPlayer={trendingPlayer}
                                isLoggedIn={isLoggedIn}
                                key={trendingPlayer.player.player}
                            />
                        );
                    })}
                </ul>
                {!data.is_all_records && !isLoading && (
                    <Link to='/trending'>
                        <button className='btn fullwidth'>View Full Trending List</button>
                    </Link>
                )}
            </Card>
        </Section>
    );
}

type TrendingPlayerItemProps = {
    trendingPlayer: TrendingPlayer;
    isLoggedIn: boolean;
};

const upArrow = <>&#8593;</>;
const downArrow = <>&#8595;</>;

export function TrendingPlayerItem({ trendingPlayer, isLoggedIn }: TrendingPlayerItemProps) {
    let icon = <></>;
    if (trendingPlayer.prev_rank && trendingPlayer.prev_rank != trendingPlayer.rank) {
        icon = trendingPlayer.prev_rank > trendingPlayer.rank ? upArrow : downArrow;
    }

    return (
        <li className='list-item trending-player-item' key={trendingPlayer.player.player}>
            <label className='flex flex-fit trending-player-rank'>{trendingPlayer.rank}.</label>
            <span className='trending-player-icon'>{icon}</span>
            <section className='flex flex-col flex-fill'>
                <p className='list-note'> {trendingPlayer.player.player} </p>
                <p className='list-title'> {trendingPlayer.analysis} </p>
            </section>
            {isLoggedIn && (
                <button className='btn tiny' onClick={() => alert('TODO')}>
                    Watch
                </button>
            )}
        </li>
    );
}
