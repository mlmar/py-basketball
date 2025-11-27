import { useStatsAnalysis } from '@/hooks/useStatsAnalysis';
import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/analysis')({
    component: RouteComponent
});

/**
 * Sample route for rendering analysis
 */
function RouteComponent() {
    const { data, isLoading, isError } = useStatsAnalysis();

    return (
        <main className='flex-col'>
            <h1> Analysis: </h1>
            {isLoading && 'Loading'}
            {isError && 'An error occurred'}
            {data?.map((projectedPlayer) => {
                return <p key={projectedPlayer.player.player}> {JSON.stringify(projectedPlayer)} </p>;
            })}
        </main>
    );
}
