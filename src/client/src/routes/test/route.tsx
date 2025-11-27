import { useStatsAverages } from '@/hooks/useStatsAverages';
import { createFileRoute } from '@tanstack/react-router';
import { useState } from 'react';

export const Route = createFileRoute('/test')({
    component: RouteComponent
});

function RouteComponent() {
    const [days, setDays] = useState<number>(10);
    const { data, isLoading, isError } = useStatsAverages(days);

    return (
        <main className='flex-col'>
            <section>
                Days:
                <input type='number' value={days || ''} onChange={(event) => setDays(parseInt(event.target.value))} />
            </section>
            {isLoading && 'Loading'}
            {isError && 'An error occurred'}
            {data?.map((player) => {
                return JSON.stringify(player);
            })}
        </main>
    );
}
