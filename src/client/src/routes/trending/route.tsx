import { BackButton } from '@/components/BackButton';
import { Header } from '@/components/Header';
import { TrendingPlayers } from '@/features/TrendingPlayers';
import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/trending')({
    component: RouteComponent
});

function RouteComponent() {
    return (
        <>
            <Header className='section'>
                <Header.TopNav>
                    <BackButton>Home</BackButton>
                    <span className='tiny-text'> Trending Players </span>
                </Header.TopNav>
                <Header.Logo>WaiverWarrior</Header.Logo>
                <Header.Tagline>
                    View trending and underrated players from the last 10 days. Updates once per day.
                </Header.Tagline>
            </Header>
            <article className='flex flex-fill'>
                <TrendingPlayers className='flex flex-fill' limit={20} />
            </article>
        </>
    );
}
