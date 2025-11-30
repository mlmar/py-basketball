import { useProjectedAnalysis } from '@/hooks/useProjectedAnalysis';
import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/analysis')({
    component: RouteComponent
});

/**
 * Sample route for rendering analysis
 */
function RouteComponent() {
    const { data, isLoading, isError } = useProjectedAnalysis();

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
