<script lang="ts">
	import { page } from '$app/state';
	import { micromark } from 'micromark';

	function getFirstViz(node: Record<string, any>) {
		let first = Object.values(node)[0];
		if (first.children) {
			return getFirstViz(first.children);
		} else {
			return first;
		}
	}

	function renderDescription(description: string) {
		return micromark(description, {
			allowDangerousHtml: false,
			allowDangerousProtocol: false
		});
	}

	let active = $state(getFirstViz(page.data));
	let descriptionVisible = $state(false);

	function selectVisualization(visualization: Record<string, any>) {
		active = visualization;
	}
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
				{@const isActive = child.index === active.index}
				<dt class="-ml-2">
					<button
						type="button"
						class="w-full cursor-pointer px-3 py-2 text-left hover:bg-gray-200"
						onclick={() => selectVisualization(child)}
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
	<div class="flex h-full min-w-48 flex-col border-r border-gray-300 bg-gray-100">
		<div class="grow overflow-auto p-2">
			{@render tree(page.data)}
		</div>
		{#if active.description}
			<button
				type="button"
				class="cursor-pointer border-t border-gray-300 px-3 py-2 text-left font-bold hover:bg-gray-200"
				onclick={() => (descriptionVisible = !descriptionVisible)}
				aria-expanded={descriptionVisible}
			>
				{descriptionVisible ? 'Hide description' : 'Show description'}
			</button>
		{/if}
	</div>
	<div class="flex min-w-0 grow flex-col">
		<iframe src={active.index} title={active.name} class="min-h-0 w-full grow"></iframe>
		{#if descriptionVisible && active.description}
			<section class="max-h-1/3 shrink-0 overflow-auto border-t border-gray-300 bg-white px-5 pb-4">
				<div class="prose max-w-none text-gray-700">
					{@html renderDescription(active.description)}
				</div>
			</section>
		{/if}
	</div>
</div>
