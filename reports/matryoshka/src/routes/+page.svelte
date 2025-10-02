<script lang="ts">
	import { page } from '$app/state';

	function getFirstViz(node: Record<string, any>) {
		let first = Object.values(node)[0];
		if (first.children) {
			return getFirstViz(first.children);
		} else {
			return first.index;
		}
	}

	let active = $state(getFirstViz(page.data));
</script>

{#snippet tree(node: Record<string, any>)}
	<dl class="pl-2">
		{#each Object.values(node) as child}
			{#if child.children}
				<dt class="mt-4 font-bold">{child.name}</dt>
				<dd class="border-l border-gray-300">
					{@render tree(child.children)}
				</dd>
			{:else}
				{@const isActive = child.index === active}
				<dt class="-ml-2">
					<button
						type="button"
						class="w-full cursor-pointer px-3 py-2 text-left hover:bg-gray-200"
						onclick={() => (active = child.index)}
						class:underline={isActive}
						class:font-bold={isActive}
						class:text-blue-600={isActive}
					>
						{child.name}
					</button>
				</dt>
			{/if}
		{/each}
	</dl>
{/snippet}

<div class="flex h-lvh">
	<div class="h-full min-w-48 overflow-auto border-r border-gray-300 bg-gray-100 p-2">
		{@render tree(page.data)}
	</div>
	<div class="grow">
		<iframe src={active} title={active} class="h-full w-full"></iframe>
	</div>
</div>
