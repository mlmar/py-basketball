import { createFileRoute } from "@tanstack/react-router";
import { Dashboard } from "~/src/features/Dashboard";

export const Route = createFileRoute("/dashboard")({
  component: Dashboard,
});
