import { TrendingPlayers } from '@/features/TrendingPlayers';
import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/trending')({
    component: RouteComponent
});

function RouteComponent() {
    return <TrendingPlayers limit={20} />;
}
