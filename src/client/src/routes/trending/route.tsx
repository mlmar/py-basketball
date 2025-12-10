import { BackButton } from '@/components/BackButton';
import { Header } from '@/components/Header';
import { TrendingPlayers } from '@/features/TrendingPlayers';
import { useTrendingplayers } from '@/hooks/useTrendingPlayers';
import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/trending')({
    component: RouteComponent
});

function RouteComponent() {
    const { data } = useTrendingplayers(null, 0);

    return (
        <>
            <Header className='section'>
                <Header.TopNav>
                    <BackButton>Home</BackButton>
                    <span className='tiny-text'> Trending Players </span>
                </Header.TopNav>
                <Header.Logo>WaiverWarrior</Header.Logo>
                <Header.Tagline>
                    View trending and underrated players from the last 10 days.
                    {data.status === 'PROCESSING' && 'Processing new daily analysis - check back in a few minutes.'}
                </Header.Tagline>
            </Header>
            <article className='flex flex-fill'>
                <TrendingPlayers className='flex flex-fill' limit={20} />
            </article>
        </>
    );
}
